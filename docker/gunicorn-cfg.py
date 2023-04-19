# -*- encoding: utf-8 -*-

# Reload the application
reload = True

# Binding Port
bind = '0.0.0.0:8000'

#workers
workers = 4

# Logger Configurations
errorlog = '-'
accesslog = '-'
loglevel = 'info'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

capture_output = True
enable_stdio_inheritance = True

# reload_extra_file = ["./app/templates/**"]