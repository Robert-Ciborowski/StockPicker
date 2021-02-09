from listing_obtainers.OTCListingObtainer import OTCListingObtainer

if __name__ == "__main__":
    from listing_obtainers.TSXListingObtainer import TSXListingObtainer
    from listing_obtainers.NASDAQListingObtainer import NASDAQListingObtainer

    # obtainer = TSXListingObtainer()
    # df = obtainer.obtain()
    # print(df)
    #
    # obtainer = NASDAQListingObtainer()
    # df = obtainer.obtain()
    # print(df)
    # print("Yay!")

    obtainer = OTCListingObtainer()
    df = obtainer.obtain()
    print(df)
