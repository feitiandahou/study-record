from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field


class WorkflowState(ABC):
    name: str

    def request_review(self, workflow: PublishingWorkflow) -> str:
        return f"cannot request review while {self.name}"

    def approve(self, workflow: PublishingWorkflow) -> str:
        return f"cannot approve while {self.name}"

    def reject(self, workflow: PublishingWorkflow) -> str:
        return f"cannot reject while {self.name}"

    @abstractmethod
    def status(self, workflow: PublishingWorkflow) -> str:
        raise NotImplementedError


class DraftState(WorkflowState):
    name = "draft"

    def request_review(self, workflow: PublishingWorkflow) -> str:
        workflow.state = ReviewState()
        return "moved to review"

    def status(self, workflow: PublishingWorkflow) -> str:
        return f"Draft: {workflow.title} is being edited"


class ReviewState(WorkflowState):
    name = "in review"

    def approve(self, workflow: PublishingWorkflow) -> str:
        workflow.state = PublishedState()
        return "published"

    def reject(self, workflow: PublishingWorkflow) -> str:
        workflow.state = DraftState()
        return "sent back to draft"

    def status(self, workflow: PublishingWorkflow) -> str:
        return f"Review: {workflow.title} is waiting for approval"


class PublishedState(WorkflowState):
    name = "published"

    def status(self, workflow: PublishingWorkflow) -> str:
        return f"Published: {workflow.title} is live"


@dataclass(slots=True)
class PublishingWorkflow:
    title: str
    state: WorkflowState = field(default_factory=DraftState)

    def request_review(self) -> str:
        return self.state.request_review(self)

    def approve(self) -> str:
        return self.state.approve(self)

    def reject(self) -> str:
        return self.state.reject(self)

    def status(self) -> str:
        return self.state.status(self)


def main() -> None:
    workflow = PublishingWorkflow("Release notes")

    print(workflow.status())
    print(workflow.request_review())
    print(workflow.status())
    print(workflow.approve())
    print(workflow.status())


if __name__ == "__main__":
    main()