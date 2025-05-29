<<<<<<< HEAD
# Công cụ Tra Giá Token từ Contract Address

Đây là một script Python cho phép bạn tra cứu giá token trực tiếp thông qua contract address bằng API của [DexScreener](https://dexscreener.com/). Công cụ này hỗ trợ nhiều blockchain phổ biến như Ethereum, BSC (Binance Smart Chain), và Solana.

## Tính năng

- **Tra cứu giá token nhanh chóng**: Lấy giá token theo contract address.
- **Tự động chọn cặp giao dịch có volume cao nhất**: Đảm bảo giá lấy ra là giá có thanh khoản tốt nhất.
- **Hỗ trợ nhiều mạng lưới**: Ethereum, BSC, Solana.
- **Kiểm tra và báo lỗi địa chỉ token**: Giúp hạn chế lỗi nhập sai địa chỉ.

## Yêu cầu

- Python 3.7+
- Các thư viện:
  - `requests`
  - `web3` (chỉ bắt buộc cho Ethereum/BSC để kiểm tra checksum address)

Cài đặt thư viện:

```bash
pip install requests web3
```

## Cách sử dụng

Chạy script:

```bash
python <tên_file.py>
```

Sau đó làm theo hướng dẫn trên màn hình:

1. **Nhập Blockchain**: Chọn một trong các giá trị `ethereum`, `bsc`, hoặc `solana`.
2. **Nhập địa chỉ token contract**: Nhập địa chỉ contract của token bạn muốn tra cứu.
3. **Xem kết quả**: Công cụ sẽ in ra giá token (USD), cặp giao dịch và mạng lưới.
4. **Tiếp tục hoặc dừng**: Nhập `1` để tra cứu tiếp, nhập `0` để kết thúc.

### Ví dụ giao diện sử dụng

```
==================================================
Công cụ tra giá Token từ Contract Address
==================================================

Nhập Blockchain (ethereum, bsc, solana): bsc
Nhập địa chỉ token contract: 0xe9e7cea3dedca5984780bafc599bd69add087d56

KẾT QUẢ:
Giá: $1.000000
Cặp giao dịch: BUSD/WBNB
Mạng lưới: bsc
---
Nhập 0 để dừng/ 1 để tiếp tục:
```

## Giải thích code chính

- **get_token_price(token_address, chain)**: Hàm này nhận token address và tên chain, gọi API DexScreener, kiểm tra địa chỉ, chọn cặp volume cao nhất, và trả về giá, cặp giao dịch, mạng lưới hoặc lỗi nếu có.
- **Kiểm tra checksum**: Với mạng Ethereum/BSC, địa chỉ sẽ được kiểm tra định dạng checksum.
- **Xử lý lỗi**: Các trường hợp lỗi như sai địa chỉ, không tìm thấy cặp giao dịch, lỗi API đều được thông báo rõ ràng.

## Lưu ý

- **DexScreener API**: Giá trị trả về phụ thuộc vào dữ liệu từ DexScreener, có thể thay đổi theo thời gian thực.
- **Địa chỉ token**: Đảm bảo nhập đúng contract address, đặc biệt với Ethereum/BSC (địa chỉ dạng checksum).
- **Không hỗ trợ token chưa list trên DexScreener**.

## License

MIT License - Tự do sử dụng và chỉnh sửa.
=======
# QuickTokenPrice
>>>>>>> ceccc042186c7e0aa7e80faf8ec2a9666e4e0c71
