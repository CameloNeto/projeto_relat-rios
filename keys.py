import dotenv

dotenv.load_dotenv()

DG_TOKEN = dotenv.get_key(".env", "DG_TOKEN")

if __name__ == "__main__":
    print("DG_TOKEN:", DG_TOKEN)
