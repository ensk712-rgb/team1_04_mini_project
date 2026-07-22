

CREATE TABLE IF NOT EXISTS menu_items (
    id TEXT PRIMARY KEY,
    restaurant_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL CHECK (price >= 0),
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- 테스트용 메뉴 데이터
INSERT INTO menu_items (restaurant_id, name, description, price) VALUES
    (1, '후라이드 치킨', '바삭하고 담백한 한 마리 치킨', 18000),
    (1, '양념 치킨', '달콤매콤 특제 양념 치킨', 19000),
    (1, '치즈볼', '고소한 모짜렐라 치즈볼 5개', 5000),
    (2, '불맛 짬뽕', '직화 향이 살아있는 해물 짬뽕', 10000),
    (2, '짜장면', '진한 춘장 소스의 짜장면', 7500),
    (2, '탕수육 소', '바삭한 탕수육과 새콤달콤 소스', 18000),
    (3, '참치 김밥', '참치와 채소가 들어간 김밥', 5000),
    (3, '떡볶이', '매콤달콤한 국물 떡볶이', 4500),
    (3, '모둠 튀김', '김말이, 오징어, 야채 튀김', 6000);
