from src import *

class tomlparser:
    @staticmethod
    def parse(content):
        if not content or not content.strip():
            return {}
            
        lines = content.replace('\r\n', '\n').replace('\r', '\n').split('\n')
        data = {}
        current_section = None
        line_number = 0
        
        for line in lines:
            line_number += 1
            original_line = line
            line = line.strip()
            
            if not line or line.startswith('#'):
                continue
            
            try:
                if line.startswith('[') and line.endswith(']'):
                    section_match = re.match(r'^\[([^\[\]]+)\]$', line)
                    if section_match:
                        current_section = section_match.group(1).strip()
                        if current_section not in data:
                            data[current_section] = {}
                    continue
                
                if '=' in line and current_section is not None:
                    parts = line.split('=', 1)
                    if len(parts) != 2:
                        continue
                        
                    key = parts[0].strip()
                    value_part = parts[1].strip()
            
                    value = tomlparser._extract_value_before_comment(value_part)
                    if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', key):
                        continue
                    
                    parsed_value = tomlparser._parse_value(value)
                    data[current_section][key] = parsed_value
                    
            except Exception:
                continue
        
        return data
    
    @staticmethod
    def _extract_value_before_comment(value_part):
        if not value_part:
            return ""
            
        in_quotes = False
        quote_char = None
        escaped = False
        
        for i, char in enumerate(value_part):
            if escaped:
                escaped = False
                continue
            
            if char == '\\' and in_quotes:
                escaped = True
                continue
            
            if char in ['"', "'"] and not in_quotes:
                in_quotes = True
                quote_char = char
            elif char == quote_char and in_quotes:
                in_quotes = False
                quote_char = None
            elif char == '#' and not in_quotes:
                return value_part[:i].strip()
        
        return value_part.strip()
    
    @staticmethod
    def _parse_value(value):
        if not value:
            return ""
        
        value = value.strip()
        
        if (value.startswith('"') and value.endswith('"')) or \
           (value.startswith("'") and value.endswith("'")):
            unquoted = value[1:-1]
            if value.startswith('"'):
                unquoted = unquoted.replace('\\"', '"')
                unquoted = unquoted.replace('\\\\', '\\')
                unquoted = unquoted.replace('\\n', '\n')
                unquoted = unquoted.replace('\\t', '\t')
                unquoted = unquoted.replace('\\r', '\r')
            return unquoted
        
        lower_value = value.lower()
        if lower_value in ['true', 'yes', 'on', '1']:
            return True
        elif lower_value in ['false', 'no', 'off', '0']:
            return False
        
        try:
            if '.' not in value and 'e' not in lower_value and 'E' not in value:
                if value.startswith('0x') or value.startswith('0X'):
                    return int(value, 16)
                elif value.startswith('0o') or value.startswith('0O'):
                    return int(value, 8)
                elif value.startswith('0b') or value.startswith('0B'):
                    return int(value, 2)
                else:
                    return int(value)
            else:
                return float(value)
            
        except ValueError:
            pass
        
        if lower_value in ['inf', '+inf', 'infinity', '+infinity']:
            return float('inf')
        elif lower_value in ['-inf', '-infinity']:
            return float('-inf')
        elif lower_value in ['nan', '+nan', '-nan']:
            return float('nan')
        
        return value

class config:
    def __init__(self):
        self.filename = 'config.toml'
        self.defaults = {
            'rpc [TURNING OFF ANVAIBLE IN PAID ONLY]': {
                'enabled': (True, 'Make RPC visible'),
                'showdata': (True, 'Shows how many tokens and proxies you have loaded')
            },
            'proxies [ANVAIBLE IN PAID ONLY]': {
                'enabled': (False, 'Enable proxy support')
            },
            'tokenonlining [ANVAIBLE IN PAID ONLY]': {
                'enabled': (True, 'Onlines your tokens on startup DISABLING THIS MAY LEAD TO CAPTCHAS OR FLAGS'),
                'delay': (0.1, 'Delay between onlines IF YOU USE A LOT TOKENS AND HAVE BAD INTERNET MAKE THIS HIGHER'),
                'status': ('random', 'The status for the tokens (online, dnd, idle, invisible, random)')
            },
            'solver [ANVAIBLE IN PAID ONLY]': {
                'README': ('For solvers to work you need proxies / GOOD PROXIES', 'readme'),
                'enabled': (False, 'Enable solver'),
                'apikey': ('your-api-key-here', 'Your solver api key'),
                'service': ('your-solver-service', 'Your solver service'),
            },
            'debug': {
                'enabled': (False, 'Enable debug mode'),
                'pause': (False, 'Pause execution for debugging')
            }
        }
        self.data = {}
        self.load()
    
    def load(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                if content.strip():
                    parseddata = tomlparser.parse(content)
                    if parseddata:
                        self.data = parseddata
                        self.validate()
                        return
                
            self.data = self._extract_defaults()
            self.save()
            
        except (IOError, OSError, UnicodeDecodeError):
            self.data = self._extract_defaults()
            self.save()

        except Exception:
            self.data = self._extract_defaults()
            self.save()
    
    def _extract_defaults(self):
        extracted = {}
        for section, values in self.defaults.items():
            extracted[section] = {}
            for key, (default_value, _) in values.items():
                extracted[section][key] = default_value
        return extracted
    
    def validate(self):
        updated = False
        for section, values in self.defaults.items():
            if section not in self.data or not isinstance(self.data[section], dict):
                self.data[section] = {}
                updated = True
            
            for key, (default_value, _) in values.items():
                if key not in self.data[section]:
                    self.data[section][key] = default_value
                    updated = True
                else:
                    old_value = self.data[section][key]
                    new_value = self.cast(old_value, default_value)
                    if old_value != new_value:
                        self.data[section][key] = new_value
                        updated = True
        
        sections_to_remove = []
        for section in self.data:
            if section not in self.defaults:
                sections_to_remove.append(section)
            else:
                keys_to_remove = []
                for key in self.data[section]:
                    if key not in self.defaults[section]:
                        keys_to_remove.append(key)
                
                for key in keys_to_remove:
                    del self.data[section][key]
                    updated = True
        
        for section in sections_to_remove:
            del self.data[section]
            updated = True
        
        if updated:
            self.save()
    
    def cast(self, value, default):
        if value is None:
            return default
        
        try:
            target_type = type(default)
            
            if target_type == bool:
                if isinstance(value, bool):
                    return value
                if isinstance(value, (int, float)):
                    return bool(value)
                if isinstance(value, str):
                    return value.lower().strip() in ['true', '1', 'yes', 'y', 'on']
                return bool(value)
                
            elif target_type == int:
                if isinstance(value, int):
                    return value
                if isinstance(value, float):
                    return int(value)
                if isinstance(value, str):
                    value = value.strip()
                    if value.lower() in ['true', 'yes', 'on']:
                        return 1
                    elif value.lower() in ['false', 'no', 'off']:
                        return 0
                    return int(float(value))
                return int(value)
                
            elif target_type == float:
                if isinstance(value, (int, float)):
                    return float(value)
                if isinstance(value, str):
                    value = value.strip()
                    if value.lower() in ['true', 'yes', 'on']:
                        return 1.0
                    elif value.lower() in ['false', 'no', 'off']:
                        return 0.0
                    return float(value)
                return float(value)
                
            elif target_type == str:
                if isinstance(value, str):
                    return value
                return str(value)
            
            return value
            
        except (ValueError, TypeError, OverflowError):
            return default
    
    def get(self, section: str, key: str, fallback=None):
        try:
            if not isinstance(section, str) or not isinstance(key, str):
                return fallback
            
            section_data = self.data.get(section)
            if not isinstance(section_data, dict):
                return fallback
            
            value = section_data.get(key, fallback)
            return value if value is not None else fallback
            
        except Exception:
            return fallback
    
    def set(self, section: str, key: str, value):
        try:
            if not isinstance(section, str) or not isinstance(key, str):
                return False
            
            if section not in self.data:
                self.data[section] = {}
            
            if not isinstance(self.data[section], dict):
                self.data[section] = {}
            
            if section in self.defaults and key in self.defaults[section]:
                default_value, _ = self.defaults[section][key]
                value = self.cast(value, default_value)
            
            self.data[section][key] = value
            self.save()
            return True
            
        except Exception:
            return False
    
    def remove(self, section: str, key: str = None):
        try:
            if not isinstance(section, str):
                return False
            
            if key is not None:
                if not isinstance(key, str):
                    return False
                section_data = self.data.get(section)
                if isinstance(section_data, dict) and key in section_data:
                    del section_data[key]
            else:
                if section in self.data:
                    del self.data[section]
            
            self.save()
            return True
            
        except Exception:
            return False
    
    def save(self):
        try:
            backup_filename = self.filename + '.backup'
            temp_filename = self.filename + '.tmp'
            with open(temp_filename, 'w', encoding='utf-8', errors='ignore') as f:
                for section, values in self.defaults.items():
                    f.write(f'\n[{section}]\n')
                    for key, (default_value, comment) in values.items():
                        actual_value = self.data.get(section, {}).get(key, default_value)
                        
                        if isinstance(actual_value, str):
                            escaped_value = actual_value.replace('\\', '\\\\').replace('"', '\\"')
                            formatted_value = f'"{escaped_value}"'
                        elif isinstance(actual_value, bool):
                            formatted_value = 'true' if actual_value else 'false'
                        elif isinstance(actual_value, (int, float)):
                            formatted_value = str(actual_value)
                        else:
                            formatted_value = f'"{str(actual_value)}"'
                        
                        f.write(f'{key} = {formatted_value}  # {comment}\n')
            
            if os.path.exists(self.filename):
                try:
                    with open(self.filename, 'r', encoding='utf-8', errors='ignore') as src:
                        with open(backup_filename, 'w', encoding='utf-8', errors='ignore') as dst:
                            dst.write(src.read())
                except Exception:
                    pass 
            
            if os.path.exists(self.filename):
                os.remove(self.filename)
            os.rename(temp_filename, self.filename)
            
            try:
                if os.path.exists(backup_filename):
                    os.remove(backup_filename)
            except Exception:
                pass
            
            return True
            
        except Exception:
            try:
                if os.path.exists(temp_filename):
                    os.remove(temp_filename)
            except Exception:
                pass
            return False

class switch:
    class rpc:
        class enabled:
            def true():
                config().set('rpc', 'enabled', True)
            
            def false():
                config().set('rpc', 'enabled', False)
        
        class showdata:
            def true():
                config().set('rpc', 'showdata', True)
            
            def false():
                config().set('rpc', 'showdata', False)
    
    class proxies:
        class enabled:
            def true():
                config.set('proxies', 'enabled', True)
            
            def false():
                config.set('proxies', 'enabled', False)
    
    class tokenonlining:
        class enabled:
            def true():
                config().set('tokenonlining', 'enabled', True)
            
            def false():
                config().set('tokenonlining', 'enabled', False)
        
        class delay:
            def set(value: float):
                config().set('tokenonlining', 'delay', float(value))
    
    class solver:
        class enabled:
            def true():
                config().set('solver', 'enabled', True)
            
            def false():
                config().set('solver', 'enabled', False)
        
        class apikey:
            def set(value: str):
                config().set('solver', 'apikey', str(value))
        
        class service:
            def set(value: str):
                config().set('solver', 'service', str(value))
    
    class debug:
        class enabled:
            def true():
                config().set('debug', 'enabled', True)
            
            def false():
                config().set('debug', 'enabled', False)
        
        class pause:
            def true():
                config().set('debug', 'pause', True)
            
            def false():
                config().set('debug', 'pause', False)

class get:
    class rpc:
        def enabled() -> bool:
            return config().get('rpc', 'enabled', True)
        
        def showdata() -> bool:
            return config().get('rpc', 'showdata', True)
    
    class proxies:
        def enabled() -> bool:
            return config().get('proxies', 'enabled', False)
    
    class tokenonlining:
        def enabled() -> bool:
            return config().get('tokenonlining', 'enabled', True)
        
        def delay() -> float:
            return float(config().get('tokenonlining', 'delay', 0.1))
        
        def status() -> str:
            return config().get('tokenonlining', 'status', 'random')
    
    class solver:
        def enabled() -> bool:
            return config().get('solver', 'enabled', False)
        
        def apikey() -> str:
            return config().get('solver', 'apikey', 'your-api-key-here')
        
        def service() -> str:
            return config().get('solver', 'service', 'teamai')
    
    class debug:
        def enabled() -> bool:
            return config().get('debug', 'enabled', False)
        
        def pause() -> bool:
            return config().get('debug', 'pause', False)