SELECT FLAVOR # --아이스크림의 맛 기준으로 조회
FROM FIRST_HALF # --상반기 주문 정보 테이블
ORDER BY TOTAL_ORDER DESC, SHIPMENT_ID
 /* 총주문량(TOTAL_ORDER) 기준으로 DESC(내림차순) 정렬 후,
    출하 번호 기준으로(SHIPMENT_ID) 오름차순 정렬 */
