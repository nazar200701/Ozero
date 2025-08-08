init python:
    def italic_tag(tag, arguments,contents):
        return [
        ( renpy.TEXT_TAG, "font=fonts/aptos-italic.ttf")
        ] + contents+[
        (renpy.TEXT_TAG, "/font")
        ]
    config.custom_text_tags["italic"] = italic_tag