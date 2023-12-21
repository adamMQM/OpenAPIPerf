import cProfile
import pstats
from unittest import mock
from unittest.mock import MagicMock, patch, AsyncMock

from lusid import ApiClient
from lusid.api.transaction_portfolios_api import TransactionPortfoliosApi
import asyncio


async def test_deserialize():
    with open("../../data/response.json") as f:
        data = f.read()

    mock_response = MagicMock()
    mock_response.status = 200
    mock_response.reason = "OK"
    mock_response.data = str.encode(data)
    mock_response.getheader.return_value = "application/json"
    mock_response_future = asyncio.Future()
    mock_response_future.set_result(mock_response)

    with patch.object(ApiClient, "request", return_value=mock_response_future):
        api = TransactionPortfoliosApi()

        profiler = cProfile.Profile()
        profiler.enable()

        await api.get_transactions(scope='a', code='a')

        profiler.disable()
        stats = pstats.Stats(profiler).sort_stats(pstats.SortKey.CUMULATIVE)
        stats.print_stats()


if __name__ == '__main__':
    asyncio.run(test_deserialize())
