import subprocess
import time
import tkinter as tk
import webbrowser

from selenium import webdriver
from selenium.webdriver.common.by import By


# Define the function to open the link
def open_link(link):
    webbrowser.open(link)


def get_nvidia_driver():
    # Load the NVIDIA website and enter the search parameters
    driver = webdriver.Firefox()
    driver.get("https://www.nvidia.com/Download/index.aspx")

    time.sleep(0.25)  # Wait for page to fully load

    # Click the search button using the GetDriver() JavaScript function
    driver.execute_script("GetDriver();")

    time.sleep(0.5)  # Wait for page to fully load

    # Scrape the tdVersion values from the search results
    results = driver.find_elements(By.XPATH, "//*[@id=\"tdVersion\"]")
    version = [result.text for result in results]

    driver_link = driver.current_url
    driver.close()

    driver_str = ''.join(c for c in str(version) if c.isdigit() or c == '.')

    return driver_link, driver_str


def current_driver():
    result = subprocess.run(['nvidia-smi', '--query-gpu=driver_version', '--format=csv,noheader'],
                            stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8').strip()

    return output


def open_window(new_driver, installed_driver, link_to_driver):
    root = tk.Tk()

    root.title("New Nvidia Driver")
    root.geometry("300x100")

    new_version_label = tk.Label(root, text=f"New Driver: {new_driver}")
    installed_version_label = tk.Label(root, text=f"Current Driver: {installed_driver}")
    new_version_label.pack()
    installed_version_label.pack()

    button = tk.Button(root, text="Download", command=lambda: open_link(link_to_driver))
    button.pack(pady=10)

    root.mainloop()


def main():
    driver_link, newest_driver = get_nvidia_driver()
    current_driver_str = current_driver()
    open_window(newest_driver, current_driver_str, driver_link)


main()
