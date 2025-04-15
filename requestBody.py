from fastapi import FastAPI, Body

app = FastAPI()

@app.post("/info/")
def create_hojunleesunsin_info(
    hojunleesunsin_info: dict = Body(
        default=None,
        example={"key": "value"},
        alias="alias",
        title="hojunleesunsin info",
        description="This is a info about hojunleesunsin",
        deprecated=False
    ),
    additional_info: dict = Body(
        default=None,
        example={"info_key": "info_value"},
        title="Additional Info",
        description="This is some additional information about hojunleesunsin",
        deprecated=False
    )
):
    return {
        "info": hojunleesunsin_info,
        "additional_info": additional_info
    }