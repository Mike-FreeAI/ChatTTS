import unittest
from ChatTTS.core import PluginManager, PluginBase
from ChatTTS.plugins.sample_plugin import SamplePlugin

class TestPluginSystem(unittest.TestCase):
    def setUp(self):
        self.plugin_manager = PluginManager()
        self.sample_plugin = SamplePlugin()

    def test_register_plugin(self):
        """Test that a plugin can be registered successfully."""
        self.plugin_manager.register_plugin(self.sample_plugin)
        self.assertIn(self.sample_plugin.name, self.plugin_manager.plugins)

    def test_execute_plugin(self):
        """Test that a registered plugin can be executed successfully."""
        self.plugin_manager.register_plugin(self.sample_plugin)
        result = self.plugin_manager.execute_plugin(self.sample_plugin.name, "test_arg", keyword="test_kwarg")
        self.assertEqual(result, "Sample Plugin executed successfully.")

if __name__ == '__main__':
    unittest.main()
