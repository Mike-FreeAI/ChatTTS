from ChatTTS.core import PluginBase

class SamplePlugin(PluginBase):
    def __init__(self):
        super().__init__("SamplePlugin")

    def execute(self, *args, **kwargs):
        print("Executing Sample Plugin with args:", args, "and kwargs:", kwargs)
        return "Sample Plugin executed successfully."
