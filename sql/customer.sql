-- Supabase SQL Editor에서 실행합니다.

CREATE TABLE IF NOT EXISTS delivery_inquiries (
    id TEXT PRIMARY KEY,
    member_id TEXT NOT NULL,
    restaurant_id TEXT NOT NULL,
    inquiry_content TEXT NOT NULL
        CHECK (char_length(trim(inquiry_content)) > 0),
    status TEXT NOT NULL DEFAULT '답변대기'
        CHECK (status IN ('답변대기', '답변완료')),
    answer TEXT,
    created_at TIMESTAMP NOT NULL
);

-- 예시 배달 문의 데이터 3건
INSERT INTO delivery_inquiries (
    id,
    member_id,
    restaurant_id,
    inquiry_content,
    status,
    answer,
    created_at
) VALUES
    (
        '20260722100000000001',
        'member-001',
        'restaurant-001',
        '주문한 음식이 아직 도착하지 않았습니다.',
        '답변대기',
        NULL,
        '2026-07-22 10:00:00'
    ),
    (
        '20260722100500000002',
        'member-002',
        'restaurant-001',
        '음식이 식어서 도착했어요.',
        '답변완료',
        '불편을 드려 죄송합니다. 고객센터에서 확인 후 도움드리겠습니다.',
        '2026-07-22 10:05:00'
    ),
    (
        '20260722101000000003',
        'member-003',
        'restaurant-002',
        '주문을 취소하고 싶습니다.',
        '답변대기',
        NULL,
        '2026-07-22 10:10:00'
    )
ON CONFLICT (id) DO NOTHING;