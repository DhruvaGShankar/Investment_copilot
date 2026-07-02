from app.services.fin_srv import get_company_info
def main():
    print("Starting test...")

    company = get_company_info("INFY.NS")

    print(company["company_name"])
    print("Price:", company["price"])
    print("Market Cap:", company["market_cap"])
    print("PE:", company["pe_ratio"])
    print("Sector:", company["sector"])

if __name__ == "__main__":
    main()