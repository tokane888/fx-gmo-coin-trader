from pydantic import BaseModel, Field


class AssetData(BaseModel):
    equity: str
    available_amount: str = Field(alias="availableAmount")
    balance: str
    estimated_trade_fee: str = Field(alias="estimatedTradeFee")
    margin: str
    margin_ratio: str = Field(alias="marginRatio")
    position_loss_gain: str = Field(alias="positionLossGain")
    total_swap: str = Field(alias="totalSwap")
    transferable_amount: str = Field(alias="transferableAmount")


class AssetsResponse(BaseModel):
    status: int
    data: AssetData
    responsetime: str
