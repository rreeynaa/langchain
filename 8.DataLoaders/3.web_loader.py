from langchain_community.document_loaders import WebBaseLoader
url="https://www.apple.com/in/iphone/?afid=p240%7Cgo~cmp-21689409814~adg-165937520614~ad-799693426722_kwd-334361787~dev-c~ext-~prd-~mca-~nt-search&cid=wwa-in-kwgo-iphone-core-iphonefamily-iphone_hero_avail_031126-iPhone_Core_Exact-iPhone_Exact"
loader=WebBaseLoader(url)
docs=loader.load()
print(len(docs))
