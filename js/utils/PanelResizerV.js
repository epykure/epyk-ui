function resizerV(e) {
    let panelCode = e.target.id.replace("_gutter", ""); window.addEventListener('mousemove', mousemove);
    window.addEventListener('mouseup', mouseup); let prevY = e.y;
    const topPanel = document.getElementById(panelCode + "_top").getBoundingClientRect();
    function mousemove(e) {
        let newY = prevY - e.y; document.getElementById(panelCode + "_top").style.height = topPanel.height - newY +"px"}
    function mouseup() {
        window.removeEventListener('mousemove', mousemove); window.removeEventListener('mouseup', mouseup)}
}