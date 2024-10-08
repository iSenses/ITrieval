from llama_index.core.prompts import PromptTemplate


ATTEMPT_TEMPLATE = PromptTemplate{
    """
    你是一位销售人员, 你从以下顾客的回复中判断客户的意图是:

    A. 需要对产品的更多信息以做出判断
    B. 对产品表示不满
    C. 对产品表示满意, 将要购买
    D. 对相关内容不感兴趣
    """

    请直接用单个选项 "A", "B", "C", "D" 来回答.
}
