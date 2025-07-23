def question_to_sql(question):
    question = question.lower()

    if "total sales" in question:
        return "SELECT SUM(total_sales) as total_sales FROM total_sales;"

    if "roas" in question or "return on ad spend" in question:
        return "SELECT SUM(ad_sales) / SUM(ad_spend) AS roas FROM ad_metrics WHERE ad_spend > 0;"

    if "highest cpc" in question or "cost per click" in question:
        return """
        SELECT item_id, ad_spend / clicks AS cpc
        FROM ad_metrics
        WHERE clicks > 0
        ORDER BY cpc DESC
        LIMIT 1;
        """

    return "ERROR: I don't understand this question. Try asking about total sales, RoAS, or CPC."
