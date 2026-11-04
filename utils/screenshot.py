from pathlib import Path


def save_screenshot(driver, name: str, output_dir: str = "reports/screenshots"):
    path = Path(output_dir)
    path.mkdir(parents=True, exist_ok=True)
    file_path = path / f"{name}.png"
    driver.save_screenshot(str(file_path))
    return file_path
