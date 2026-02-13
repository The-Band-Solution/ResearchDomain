import os
import sys
import subprocess
from hatchling.builders.hooks.plugin.interface import BuildHookInterface

class CustomBuildHook(BuildHookInterface):
    def initialize(self, version, build_data):
        print("Running AI Reference Generator...")
        # self.root is available in BuildHookInterface
        script_path = os.path.join(self.root, "scripts", "generate_ai_reference.py")
        
        # Execute the script
        result = subprocess.run([sys.executable, script_path], check=False, capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"Warning: Failed to generate AI Reference:\n{result.stderr}")
        else:
            print(f"AI Reference generated successfully.")

