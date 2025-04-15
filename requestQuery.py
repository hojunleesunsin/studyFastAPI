from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/hojunleesunsin/")
def read_items(
    string_query: str = Query(default="hojun", min_length=1, max_length=10, regex="^[a-zA-Z]+$", title="String", example="hohoho"),
    number_query: float = Query(default=177.8, ge=0.5, le=200.0, title="Number", example=5.5)
):
    return {
        "string_query_handled": string_query,
        "number_query_handled": number_query
    }
