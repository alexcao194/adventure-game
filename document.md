#  API Document
Tài liệu được viết để các thành viên nắm bắt được cách sử dụng các thành phần có sẵn trong tầng framework.

## Assets
Các assets được tổ chức ở tầng cùng tên, bao gồm các thư mục con : `animation, texture, font, audio, ...` tương ứng. Trong đó cần lưu ý cách tổ chức:
- Các assets của **animation** được đặt trong thư mục có **tên là tên của animation**, đánh số các **frame** từ 0 -> hết. 
Ví dụ: thư mục "idle" chứa các ảnh 0.png, 1.png, 2.png, 3. png
- Ngay sau khi thêm assets, cần định nghĩa đường dẫn của asset tương ứng vào file [assets.py](https://github.com/DawnHNguyen/BTL-Python-2023/blob/develop/src/configs/assets.py).
- Animation cần dẫn tới thư mục, các tài nguyên khác dẫn tới file tài nguyên.
	```python
	class Assets(Singleton):
	    ani_idle = 'assets/animations/idle/' # phải kết thúc bằng '/'
	    tt_block = 'assets/textures/block.png'
	    au_fire = 'assets/audios/fire.wav'
	    fnt_pixel = 'assets/fonts/pixel.ttf'
	```
## State
Trong dự án, chúng ta coi mỗi màn hình là một State, các lớp kế thừa **BaseState** đều được cung cấp tất cả mọi thứ để khởi tạo một màn hình.  <br>
Có thể quản lý các màn hình bằng **StateMachine** (push, pop)
## Entity
Các entity là các thực thể ở trong màn hình play của game, bao gồm các nhân vật, khối gạch, đạn, ... 
Có 2 cách vẽ entity: 
- Sử dụng hệ thống animation với **Animation Manager**
	```python
	self.animation_manager = AnimationManager(
	        action_animation = {
	            'roll': ActionAnimation(Assets.roll, 5, self, delay=2),
	            'test': ActionAnimation(Assets.test, 10, self, delay=2),
	        },
	        repeat_animation = {
	            'walk': RepeatAnimation(Assets.walk, 8, self, delay=2),
	            'idle': RepeatAnimation(Assets.idle, 6, self, delay=2),
	            'test2': RepeatAnimation(Assets.test2, 10, self, delay=2),
	        },
	        current_animation = 'idle'
	    )
	```
	Trong đó tham số thứ 3 phải là tên một RepeatAnimation đại diện cho trạng thái khởi tạo của nhân vật.

- Sử dụng hệ thống Texture:
	```python
	self.texture = Texture(texture=texture, entity=self)
	```

## Widget
Là các thành phần trong các màn hình như menu, settings, ... bao gồm các button, text, ... 

## Localization
Là hệ thống dịch ngôn ngữ, được sử dụng để dịch các text trong game sang các ngôn ngữ khác nhau.
- Các ngôn ngữ được định nghĩa trong folder **strings** với đuôi là **.json**.
- Các text được định nghĩa trong các file json tương ứng, với key là tên của text, value là nội dung của text.
- Sau khi thêm hoặc sửa các file json, chạy file **__gen__.py** để sinh ra các file python tương ứng.
- Sử dụng:
	'''python
	from framework.framework import Localization as S
	text = S().key # get text with key
	S.language = 'vi' # change locale
	'''


Sample code: [Sample code](example.md)