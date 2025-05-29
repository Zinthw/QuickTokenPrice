import requests
from web3 import Web3
from typing import Optional, Dict, Union

# API DexScreener để lấy giá token
DEX_SCREENER_API = "https://api.dexscreener.com/latest/dex/tokens/"

def get_token_price(token_address: str, chain: Optional[str] = None) -> Dict[str, Union[float, str, None]]:
    try:
        # Kiểm tra địa chỉ token (không áp dụng cho Solana)
        if chain != "solana":
            try:
                token_address = Web3.to_checksum_address(token_address)
            except:
                return {"error": "Địa chỉ token không hợp lệ"}

        # Gọi DexScreener API
        response = requests.get(f"{DEX_SCREENER_API}{token_address}", timeout=10).json()
        
        if "pairs" not in response or len(response["pairs"]) == 0:
            return {"error": "Không tìm thấy cặp giao dịch trên DexScreener"}

        # Lấy cặp giao dịch có volume cao nhất
        pair = max(response["pairs"], key=lambda x: float(x.get("volumeUsd", 0)))
        price = float(pair.get("priceUsd", 0))
        
        if price <= 0:
            return {"error": "Giá token không khả dụng"}

        return {
            "price": price,
            "pair": f"{pair['baseToken']['symbol']}/{pair['quoteToken']['symbol']}",
            "chain": pair.get("chainId", chain),
            "error": None,
        }

    except requests.exceptions.RequestException as e:
        return {"error": f"Lỗi kết nối API: {str(e)}"}
    except Exception as e:
        return {"error": f"Lỗi không xác định: {str(e)}"}

if __name__ == "__main__":
    running = 1
    print("==================================================")
    print("Công cụ tra giá Token từ Contract Address")
    print("==================================================\n")

    while running:
        chain = input("Nhập Blockchain (ethereum, bsc, solana): ")
        address = input("Nhập địa chỉ token contract: ")

        result = get_token_price(address, chain)
        print(f"\nKẾT QUẢ:")
        if result.get("price"):
            print(f"Giá: ${result['price']:.6f}")
            print(f"Cặp giao dịch: {result['pair']}")
            print(f"Mạng lưới: {result['chain']}")
        else:
            print(f" Lỗi: {result.get('error', 'Unknown error')}")
        print("---")
        running = input("Nhập 0 để dừng/ 1 để tiếp tục: ")