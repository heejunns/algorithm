// 프로그래머스 같은 숫자는 싫어
function solution(arr) {
  const answer = [];

  arr.forEach((element) => {
    if (answer.length === 0) {
      answer.push(element);
    } else if (answer[answer.length - 1] !== element) {
      answer.push(element);
    }
  });
  return answer;
}
