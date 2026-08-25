# 检查登录
# anaconda login
# 检查环境
conda activate env_cnrdiff
# 检查安装
# conda install -c conda-forge conda-build anaconda-client
# 清除缓存
conda build purge
# 构建conda包并上传
conda build conda_recipe/
anaconda upload $(conda build --output conda_recipe/)
# 检查上传结果
# conda install kongolou::cnrdiff
