from blinker import Namespace

_signals = Namespace()

#: Called before a template is rendered, connection functions
# should have a signature of Callable[[Quart, Template, dict], None]
before_render_template = _signals.signal('before-render-template')

#: Called when a template has been rendered, connected functions
# should have a signature of Callable[[Quart, Template, dict], None]
template_rendered = _signals.signal('template-rendered')

#: Called just after the request context has been created, connected
# functions should have a signature of Callable[[Quart], None]
request_started = _signals.signal('request-started')

#: Called after a response is fully finalised, connected functions
# should have a signature of Callable[[Quart, Response], None]
request_finished = _signals.signal('request-finished')

#: Called as the request context is teared down, connected functions
# should have a signature of Callable[[Quart, Exception], None]
request_tearing_down = _signals.signal('request-tearing-down')

#: Called if there is an exception handling the request, connected
# functions should have a signature of Callable[[Quart, Exception], None]
got_request_exception = _signals.signal('got-request-exception')

#: Called as the application context is teared down, connected functions
# should have a signature of Callable[[Quart, Exception], None]
appcontext_tearing_down = _signals.signal('appcontext-tearing-down')

#: Called when the app context is pushed, connected functions should
# have a signature of Callable[[Quart], None]
appcontext_pushed = _signals.signal('appcontext-pushed')

#: Called when the app context is poped, connected functions should
# have a signature of Callable[[Quart], None]
appcontext_popped = _signals.signal('appcontext-popped')

#: Called on a flash invocation, connection functions
# should have a signature of Callable[[Quart, str, str], None]
message_flashed = _signals.signal('message-flashed')
