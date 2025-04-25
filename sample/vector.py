import pygame
import math

# Pygameの初期化
pygame.init()

# 画面の設定
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ベクトルドラッグ")

# ベクトルの初期設定
origin = (WIDTH // 2, HEIGHT // 2)  # 原点
length_a = 100  # ベクトルの長さ
angle_a = math.radians(30)  # ベクトルの角度（30度）

# ベクトルの計算
def vec_from_angle(angle, length):
    return math.cos(angle) * length, math.sin(angle) * length

# ベクトルAを計算
vec_a = vec_from_angle(angle_a, length_a)

# ベクトルを描画する関数
def draw_vector():
    pygame.draw.line(screen, (255, 0, 0), origin, (origin[0] + vec_a[0], origin[1] + vec_a[1]), 3)
    # 矢印の先端を描画
    arrow_size = 10
    end_x = origin[0] + vec_a[0]
    end_y = origin[1] + vec_a[1]
    angle = math.atan2(vec_a[1], vec_a[0])
    left = (end_x + math.cos(angle + math.pi / 4) * arrow_size,
            end_y + math.sin(angle + math.pi / 4) * arrow_size)
    right = (end_x + math.cos(angle - math.pi / 4) * arrow_size,
             end_y + math.sin(angle - math.pi / 4) * arrow_size)
    pygame.draw.polygon(screen, (255, 0, 0), [left, (end_x, end_y), right])

# マウス操作の状態
dragging = False
drag_start = None

# ゲームループ
running = True
while running:
    screen.fill((255, 255, 255))  # 画面を白で塗りつぶす

    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # マウスがクリックされたとき
            if pygame.mouse.get_pressed()[0]:  # 左クリック
                drag_start = pygame.mouse.get_pos()
                dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            # マウスが離されたとき
            dragging = False
        elif event.type == pygame.MOUSEMOTION:
            # マウスが動いたとき
            if dragging:
                dx, dy = pygame.mouse.get_pos()
                vec_a = vec_from_angle(math.atan2(dy - drag_start[1], dx - drag_start[0]), length_a)
                drag_start = pygame.mouse.get_pos()

    # ベクトルを描画
    draw_vector()

    # 画面更新
    pygame.display.flip()

# Pygameを終了
pygame.quit()
