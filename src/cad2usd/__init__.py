import os
import subprocess
import sys
from pathlib import Path
import glob

BUILD_PLATFORMS = {
    "windows-x86_64": "kit.exe",
    "linux-x86_64": "kit.sh",
}
REPO_ROOT = Path(__file__).parent.parent.parent
print(REPO_ROOT)

def find_hoops_main_script(kit_build_path: Path) -> str:
    """
    Dynamically find the hoops_main.py script in the extscache directory.

    Args:
        kit_build_path: Path to the kit build directory

    Returns:
        str: Full path to hoops_main.py

    Raises:
        FileNotFoundError: If hoops_main.py cannot be found
    """
    extscache_path = kit_build_path / "extscache"

    # Search for directories matching the pattern omni.services.convert.cad-*
    pattern = str(extscache_path / "omni.services.convert.cad-*")
    matching_dirs = glob.glob(pattern)

    if not matching_dirs:
        raise FileNotFoundError(f"No directories matching 'omni.services.convert.cad-*' found in {extscache_path}")

    # Take the first matching directory (there should typically be only one)
    cad_service_dir = Path(matching_dirs[0])

    # Construct the full path to hoops_main.py
    hoops_main_path = cad_service_dir / "omni" / "services" / "convert" / "cad" / "services" / "process" / "hoops_main.py"

    if not hoops_main_path.exists():
        raise FileNotFoundError(f"hoops_main.py not found at expected location: {hoops_main_path}")

    return str(hoops_main_path)



def main() -> None:
    print("Hello from cad2usd!")

    print(f"Building for platforms: {BUILD_PLATFORMS}")

    kit_exe_path: Path = None
    kit_build_path: Path = None
    for platform, exe in BUILD_PLATFORMS.items():
        kit_exe_path = REPO_ROOT / "kit" / "_build" / platform / "release" / "kit" / exe
        if  kit_exe_path.exists():
            kit_build_path = REPO_ROOT / "kit" / "_build" / platform / "release"
            print(f"Kit executable found at: {kit_exe_path}")
            break

    try:
        script_path = find_hoops_main_script(kit_build_path)
        print(f"Found hoops_main.py at: {script_path}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)

    input_path = str(REPO_ROOT / "nova_carter_full.step")
    output_path = str(REPO_ROOT / "nova_carter_full.usd")
    config_path = str(REPO_ROOT / "config.json")
    script_args = f'{script_path} --input-path {input_path} --output-path {output_path} --config-path {config_path}'
    cmd = [
        kit_exe_path,
        "--allow-root",
        "--enable", "omni.kit.converter.hoops_core",
        "--exec",
        "--/app/fastShutdown=1",
        f"{script_args}",
        "--info"
    ]
    print(cmd)
    subprocess.run(cmd, cwd=REPO_ROOT)

if __name__ == "__main__":
    main()
