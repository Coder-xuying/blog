#!/bin/bash

# 设置 GitHub 用户名和仓库信息
github_username="Coder-xuying"
repository_name="blog"

# 设置提交消息，默认为 "Update"
commit_message="Update"

# 设置本次提交的作者名为 "xy"
git config user.name "xy"

# 检查是否提供了提交消息参数
if [[ $# -gt 0 ]]; then
    commit_message="$1"
fi

# 执行 git add 命令将要提交的文件添加到暂存区
echo "Adding files to staging area..."
git add .

# 执行 git commit 命令，并指定作者名
echo "Committing changes with message: $commit_message"
git commit -m "$commit_message"

# 执行 git push 命令推送更改到 GitHub 仓库，并检查推送结果
echo "Pushing changes to GitHub repository..."
if git push "git@github.com:$github_username/$repository_name.git"; then
    echo "Push successful!"
else
    echo "Push failed. Check the reason."
fi
