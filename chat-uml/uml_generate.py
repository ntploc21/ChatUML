'''The file that help with generating the UML diagram from the GPT-3 API'''

from plantweb.render import render


def get_uml_diagram(content):
    '''Generate UML diagram from PlantUML code
    
    Args:
        content (str): The PlantUML code
    
    Returns:
        str: The SVG code of the diagram
    '''
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
