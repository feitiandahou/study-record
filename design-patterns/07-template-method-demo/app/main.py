from abc import ABC, abstractmethod


class DeploymentSummary(ABC):
    def build(self, service: str, version: str) -> str:
        steps = [
            self.start(service, version),
            self.run_checks(service),
            self.publish(service, version),
            self.finish(service, version),
        ]
        return self.format_summary(service, version, steps)

    def start(self, service: str, version: str) -> str:
        return f"prepare {service} {version}"

    def run_checks(self, service: str) -> str:
        return f"verify health checks for {service}"

    def publish(self, service: str, version: str) -> str:
        return f"release {service} {version}"

    def finish(self, service: str, version: str) -> str:
        return f"announce {service} {version}"

    @abstractmethod
    def format_summary(self, service: str, version: str, steps: list[str]) -> str:
        raise NotImplementedError


class EmailDeploymentSummary(DeploymentSummary):
    def format_summary(self, service: str, version: str, steps: list[str]) -> str:
        body = "\n".join(f"- {step}" for step in steps)
        return f"Subject: {service} {version} deployed\n{body}"


class SlackDeploymentSummary(DeploymentSummary):
    def format_summary(self, service: str, version: str, steps: list[str]) -> str:
        body = " | ".join(steps)
        return f"slack: [{service}@{version}] {body}"


def main() -> None:
    email_summary = EmailDeploymentSummary()
    print(email_summary.build("billing-api", "v1.4.2"))
    print()

    slack_summary = SlackDeploymentSummary()
    print(slack_summary.build("billing-api", "v1.4.2"))


if __name__ == "__main__":
    main()