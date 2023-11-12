import sys


def robot_remove(list_of_robots: str, limit: str) -> int:
    # Сортировка выполняется за время O(n*log(n)) в худшем случае - Timsort
    list_of_robots: list = sorted(
        [int(robot) for robot in list_of_robots.split(' ')]
    )
    limit: int = int(limit)
    left: int = 0
    right: int = len(list_of_robots) - 1
    count: int = 0

    # Использовался метод двух указателей
    for i in range(limit, 1, -1):
        while left < right:
            result = list_of_robots[left] + list_of_robots[right]
            if result == limit:
                list_of_robots.pop(right)
                list_of_robots.pop(left)
                right -= 2
                count += 1
            elif result > limit:
                right -= 1
            else:
                left += 1
        if len(list_of_robots) == 0:
            break
        left = 0
        right = len(list_of_robots) - 1
        limit -= 1
    return count + len(list_of_robots)


if __name__ == '__main__':
    list_of_robots: str = sys.stdin.readline().rstrip()
    limit: str = sys.stdin.readline().rstrip()
    robot_remove(list_of_robots, limit)
