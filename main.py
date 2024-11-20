import sys
import yt_dlp  # yt_dlp 라이브러리 사용
import subprocess

# macOS 알림을 띄우는 함수
def show_notification(title, message):
    script = f'display notification "{message}" with title "{title}"'
    subprocess.call(["osascript", "-e", script])

# 유튜브 링크가 첫 번째 인자로 전달됨
if len(sys.argv) > 1:
    url = sys.argv[1].strip()  # 입력된 링크에서 앞뒤 공백 제거
    # 입력받은 URL을 알림으로 출력
    # show_notification("입력된 URL 확인", f"입력된 URL: {url}")
    print(f"다운로드할 유튜브 링크: {url}")
else:
    show_notification("다운로드 실패", "유효한 유튜브 링크가 제공되지 않았습니다.")
    print("유효한 유튜브 링크가 제공되지 않았습니다.")
    sys.exit(1)

# yt-dlp 옵션 설정
ydl_opts = {
    'format': 'best', # 최고의 품질로 다운로드
    'outtmpl': '~/Downloads/%(title)s_%(id)s.%(ext)s', # 맥의 다운로드 폴더로 경로 설정
    'quiet': False, # 로깅 출력
    'overwrites': False,
}


# yt-dlp를 사용한 비디오 다운로드 및 성공/실패 알림
try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    show_notification("다운로드 성공", "YouTube 비디오가 성공적으로 다운로드되었습니다.")
except Exception as e:
    show_notification("다운로드 실패", f"오류가 발생했습니다: {e}")
    print(f"오류가 발생했습니다: {e}")
