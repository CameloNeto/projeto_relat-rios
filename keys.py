import dotenv

dotenv.load_dotenv()

DG_TOKEN = dotenv.get_key(".env", "DG_TOKEN")
NEOFIN_API_KEY = dotenv.get_key(".env", "NEOFIN_API_KEY")
NEOFIN_SECRET_KEY = dotenv.get_key(".env", "NEOFIN_SECRET_KEY")

if __name__ == "__main__":
    print("DG_TOKEN:", DG_TOKEN)
    print("NEOFIN_API_KEY:", NEOFIN_API_KEY)
    print("NEOFIN_SECRET_KEY:", NEOFIN_SECRET_KEY)