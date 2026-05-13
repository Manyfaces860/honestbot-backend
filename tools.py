from agents import function_tool
from logger import logger, logging
from constants import INDEX_NAME, NAMESPACE, TOP_K
from setup import pc, QueryResponse
from embedding import get_embedding

@function_tool
def get_context(query: str) -> str:
    logger.log(level=logging.INFO, msg='getting context from vdb')
    index = pc.Index(INDEX_NAME)
    
    dense_query_embedding, sparse_query_embedding = get_embedding(query, "query")
    results: QueryResponse = QueryResponse()
    for d, s in zip(dense_query_embedding, sparse_query_embedding):
        query_response = index.query(
            namespace=NAMESPACE,
            top_k=TOP_K,
            vector=d['values'],
            sparse_vector={'indices': s['sparse_indices'], 'values': s['sparse_values']},
            include_values=False,
            include_metadata=True
        )
        results = query_response

    context = ""
    logger.log(level=logging.INFO, msg=f"results: {results}")
    for hits in results.matches:
        assert hits.metadata is not None
        context += "\n" + str(hits.metadata.get('text', ''))
    return context