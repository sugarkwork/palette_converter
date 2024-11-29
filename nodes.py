import os

class PaletteConverter:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "palette": ("STRING", {"default": ""}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("output",)

    FUNCTION = "convert"

    CATEGORY = "string"

    OUTPUT_NODE = True

    @staticmethod
    def hex_to_rgb(hex_color):
        # '#' を除去して、16進数の文字列を取得
        hex_color = hex_color.lstrip('#')
        # 16進数を10進数に変換
        return (
            int(hex_color[0:2], 16),
            int(hex_color[2:4], 16),
            int(hex_color[4:6], 16)
        )

    def convert(self, palette:str):
        rgb_colors = [self.hex_to_rgb(color) for color in palette]
        return (str(rgb_colors), )


NODE_CLASS_MAPPINGS = {
    "PaletteConverter": PaletteConverter,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PaletteConverter": "PaletteConverter",
}
