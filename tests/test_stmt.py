from app.services.stmt_srv import get_fin_stmt


def main():

    statements = get_fin_stmt("INFY.NS")

    print(statements["income_statement"])

    print()

    print(statements["balance_sheet"])

    print()

    print(statements["cash_flow"])


if __name__ == "__main__":
    main()