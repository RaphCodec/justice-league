import requests
import xml.etree.ElementTree as ET


def download_xml_data(url, filename="data.xml"):
    """Downloads XML data from a URL and saves it to a file.

    Args:
        url: The URL to download the XML data from.
        filename: The name of the file to save the XML data to.
    """
    try:
        response = requests.get(url)
        response.raise_for_status() 

        with open(filename, "wb") as file:
            file.write(response.content)
        print(f"XML data downloaded successfully to {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading XML data: {e}")
    except IOError as e:
        print(f"Error writing to file: {e}")


def parse_xml_data(filename="data.xml"):
    """Parses XML data from a file.

    Args:
        filename: The name of the file containing the XML data.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        return root
    except FileNotFoundError:
        print(f"Error: File not found: {filename}")
        return None
    except ET.ParseError as e:
        print(f"Error parsing XML data: {e}")
        return None