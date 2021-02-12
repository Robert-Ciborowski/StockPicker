from listing_obtainers.OTCListingObtainer import OTCListingObtainer
from listing_obtainers.TSVListingObtainer import TSVListingObtainer

if __name__ == "__main__":
    from listing_obtainers.TSXListingObtainer import TSXListingObtainer
    from listing_obtainers.NASDAQListingObtainer import NASDAQListingObtainer

    # obtainer = TSXListingObtainer()
    # df = obtainer.obtain()
    # df.to_csv("tsx.csv")
    # print(df)

    obtainer = TSVListingObtainer()
    df = obtainer.obtain()
    print(df)

    # obtainer = NASDAQListingObtainer()
    # df = obtainer.obtain()
    # print(df)
    # print("Yay!")

    # obtainer = OTCListingObtainer()
    # df = obtainer.obtain()
    # print(df)
