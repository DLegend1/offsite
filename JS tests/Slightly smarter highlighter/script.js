const rules = document.getElementById("rules");
const editable = document.getElementById("editable");

const keywordsList = [
    {
        keywords: "dacko|legend",
        className: "dacko"
    },
    {
        keywords: "this|const|break",
        className: "code"
    },
    {
        keywords: "foksmash|vanker|steiner",
        className: "gunther"
    }
]

function updateText(refocusText = true){
    let newContent = editable.textContent.replace(/&nbsp;/g, ' ');

    for(let keywordGroup of keywordsList){
        let regex = new RegExp(`(${keywordGroup.keywords})`, 'g')
        if(newContent.match(regex)){
            newContent = newContent.replace(regex, `<span class="${keywordGroup.className}">$1</span>`)
        }
    }
    editable.innerHTML = newContent

    if(refocusText){
        editable.focus()
        document.getSelection().collapse(editable, editable.childNodes.length)
    }
}

function init(){
    let index = 0;
    for(let keywordGroup of keywordsList){
        let ruleName = document.createElement('input')
        ruleName.dataset.type = 'key'
        ruleName.value = keywordGroup.keywords;
        
        let ruleStyle = document.createElement('input')
        ruleStyle.value = keywordGroup.className

        let container = document.createElement('div')
        container.dataset.id = index;
        container.appendChild(ruleName)
        container.appendChild(ruleStyle)

        container.addEventListener("input", function(event){
            let input = event.target.closest('input')
            if(!input) return;
            if(input.dataset.type){
                updateKeywords(this.dataset.id, input.value)
            } else {
                updateClassName(this.dataset.id, input.value)
            }
            updateText(false)
        })

        rules.appendChild(container)
        index++;
    }
}

function updateKeywords(index, value){
    value = value.replace(/^\|+|\|+$/g)
    keywordsList[index].keywords = value;
}

function updateClassName(index, value){
    keywordsList[index].className = value;
}

function debounce(func, wait, immediate) {
	var timeout;
	return function() {
		var context = this, args = arguments;
		var later = function() {
			timeout = null;
			if (!immediate) func.apply(context, args);
		};
		var callNow = immediate && !timeout;
		clearTimeout(timeout);
		timeout = setTimeout(later, wait);
		if (callNow) func.apply(context, args);
	};
};

//ENTRY POINT
init()
var debouncedUpdate = debounce(updateText, 600)
editable.addEventListener('input', debouncedUpdate)