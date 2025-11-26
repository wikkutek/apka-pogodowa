import dotenv
import os
dotenv.load_dotenv()

#w tym pliku są wszystkie nasze konfiguracje

class Config: #nazwy klas piszemy z dużych liter
    QUERY = os.getenv("QUERY")
    API_KEY = os.getenv("API_KEY")
    XLSX_PATH = "pogoda.xlsx"
