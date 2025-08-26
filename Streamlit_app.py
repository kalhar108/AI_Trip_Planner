import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from agent.agentic_workflow import GraphBuilder  # your module from screenshots

app = FastAPI()


class QueryRequest(BaseModel):
    query: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/query")
async def query_travel_agent(query: QueryRequest):
    try:
        # Build your graph / reactive app
        graph = GraphBuilder(model_provider="groq")
        react_app = graph()  # GraphBuilder is callable in your code

        # (Optional) render and save the Mermaid graph PNG, as in your screenshot
        try:
            png_graph = react_app.get_graph().draw_mermaid_png()
            with open("my_graph.png", "wb") as f:
                f.write(png_graph)
            print(f"Graph saved as 'my_graph.png' in {os.getcwd()}")
        except Exception:
            # Don't fail the request if visualization isn't available
            pass

        # The app expects {"messages": [...]} and you pass the user query
        messages = {"messages": [query.query]}

        # Run the graph
        output = react_app.invoke(messages)

        # If output is a dict with "messages", return last message content
        if isinstance(output, dict) and "messages" in output and output["messages"]:
            final_output = output["messages"][-1].content
        else:
            final_output = str(output)

        return {"answer": final_output}

    except Exception as e:
        # Error handling identical to your screenshot
        return JSONResponse(status_code=500, content={"error": str(e)}) 