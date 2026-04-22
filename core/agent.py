# 无障碍适配Agent
class AdaptAgent:
    @staticmethod
    def adapt_text(text: str) -> str:
        text = text.replace("然后", "").replace("就是说", "")
        sentences = text.split("。")
        return "。\n".join([s.strip() for s in sentences if s.strip()])

# 知识梳理Agent
class KnowledgeAgent:
    @staticmethod
    def build_mind_map(text: str) -> str:
        return f"【重点】{text[:30]}..."

# 学情反馈Agent
class FeedbackAgent:
    @staticmethod
    def get_student_report(lesson_id: str) -> dict:
        return {
            "lesson_id": lesson_id,
            "weak_points": ["术语理解", "长句阅读"],
            "suggest": "多看手语视频+短句复习"
        }

# Agent 流水线
class AgentPipeline:
    @staticmethod
    def run(text: str) -> dict:
        adapted = AdaptAgent.adapt_text(text)
        mind = KnowledgeAgent.build_mind_map(adapted)
        return {
            "adapted_text": adapted,
            "mind_map": mind,
            "sign_script": adapted
        }