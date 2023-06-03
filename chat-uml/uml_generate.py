from plantweb.render import render


def get_uml_diagram(content):
    try:
        output = render(
            content,
            engine='plantuml',
            format='svg',
            cacheopts={
                'use_cache': False
            }
        )
        return output[0].decode()
    except:
        return ""
