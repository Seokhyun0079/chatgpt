from langchain_community.embeddings import OpenAIEmbeddings 
embeddings = OpenAIEmbeddings()
query = "AWSのS3からデータを読み込むためのDocumentLoaderはありますか？" 
vector = embeddings. embed_query( query) 
print( len( vector)) 
print( vector)



