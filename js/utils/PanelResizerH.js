function resizerH(e) {
    let panelCode = e.target.id.replace("_gutter", ""); window.addEventListener('mousemove', mousemove);
    window.addEventListener('mouseup', mouseup); let prevX = e.x;
    const leftPanel = document.getElementById(panelCode + "_left").getBoundingClientRect();
    function mousemove(e) {
        let newX = prevX - e.x; document.getElementById(panelCode + "_left").style.width = leftPanel.width - newX +"px"}
    function mouseup() {
        window.removeEventListener('mousemove', mousemove); window.removeEventListener('mouseup', mouseup)}
}