# 📌 Decktitle – Show Deck Name in Anki Window Title

Hiển thị tên deck hoặc subdeck đang học ngay trên **tiêu đề cửa sổ Anki**.  
Tự động khôi phục tiêu đề mặc định khi quay về màn hình chính.

---

## ✨ Tính năng chính

✅ Khi bắt đầu học thẻ: tiêu đề đổi thành:

```
[Tên người dùng] - Anki - [Biểu tượng] [Tên Deck/Subdeck]
```

✅ Khi quay lại màn hình chính (Deck Browser): tiêu đề trở lại mặc định:

```
[Tên người dùng] - Anki
```

✅ Cho phép tùy chỉnh tiêu đề, biểu tượng, định dạng hiển thị.

---

## ⚙️ Cấu hình (Tools → Add-ons → Decktitle → Config)

Bạn có thể chỉnh các tùy chọn sau trong khung cấu hình:

```json
{
  "enable_title": true,
  "icon": "📚",
  "title_color": "#FF0000",
  "title_format": "{profile} - Anki - {icon} {deck}"
}
```

### 🔹 Giải thích:

| Khóa | Ý nghĩa |
|------|--------|
| `enable_title` | Bật/tắt tính năng hiển thị tiêu đề tùy chỉnh |
| `icon`         | Biểu tượng hiển thị kèm tên deck |
| `title_color`  | (Chưa dùng) – Dự phòng cho tính năng màu sắc |
| `title_format` | Định dạng hiển thị, có thể dùng `{profile}`, `{deck}`, `{icon}` |

---

## 🧪 Ví dụ hiển thị

```text
DrPhan6.5IELTS - Anki - 📚 Listening Vocabulary::Talking about gifts
```

---

## 🛠 Tương thích

- ✅ Hoạt động tốt với Anki 2.1.35+ đến 25.02.5
- ✅ Tương thích Windows/macOS/Linux
- ✅ Không xung đột với các addon phổ biến như Fastbar, AnkiConnect, Leaderboard...

---

## 🧑‍💻 Cách hoạt động

- `reviewer_did_show_question`: khi bắt đầu học → thay đổi tiêu đề
- `state_did_change`: khi quay về deck browser → khôi phục tiêu đề mặc định

---

## 📂 Cấu trúc addon

```
Decktitle/
├── __init__.py
├── meta.json
├── config.md   ← phần mô tả hiển thị bên phải cấu hình
```

---

## ❤️ Gợi ý biểu tượng

📚 💡 🚀 🧠 🔥 ✅ ✨ ⏱️ 📝 🎯

---
