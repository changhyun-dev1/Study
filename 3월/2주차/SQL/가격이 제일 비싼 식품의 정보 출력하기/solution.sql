# 첫 번째 방법
SELECT *
FROM FOOD_PRODUCT
WHERE PRICE = (SELECT MAX(PRICE) FROM FOOD_PRODUCT);

# 두 번째 방법
SELECT *
FROM FOOD_PRODUCT
ORDER BY PRICE DESC
LIMIT 1;
