import voyageai
import dotenv
import os
import numpy as np

# Load environment variables from .env file
dotenv.load_dotenv()

api_key = os.environ.get("VOYAGE-AI-KEY")

vo = voyageai.Client(api_key=api_key)

documents = [
    "The Mediterranean diet emphasizes fish, olive oil, and vegetables, believed to reduce chronic diseases.",
    "Photosynthesis in plants converts light energy into glucose and produces essential oxygen.",
    "20th-century innovations, from radios to smartphones, centered on electronic advancements.",
    "Rivers provide water, irrigation, and habitat for aquatic species, vital for ecosystems.",
    "Apple’s conference call to discuss fourth fiscal quarter results and business updates is scheduled for Thursday, November 2, 2023 at 2:00 p.m. PT / 5:00 p.m. ET.",
    "Shakespeare's works, like 'Hamlet' and 'A Midsummer Night's Dream,' endure in literature.",
]
# This will automatically use the environment variable VOYAGE_API_KEY.
# Alternatively, you can use vo = voyageai.Client(api_key="<your secret key>")

doc_embds = vo.embed(documents, model="voyage-2", input_type="document").embeddings

query = "Shakespeares works?"

query_embd = vo.embed([query], model="voyage-2", input_type="query").embeddings[0]

similarities = np.dot(doc_embds, query_embd)

retrieved_id = np.argmax(similarities)
print(documents[retrieved_id])
