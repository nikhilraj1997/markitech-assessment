const itemComparsionElements = document.getElementsByClassName(
  "outlook-item__comparison"
)

const itemcComparisonInterval = setInterval(() => {
  const itemComparisonElementsItems = Array.prototype.slice.call(
    itemComparsionElements
  )

  if (itemComparsionElements) {
    let comparisonMaxHeight = 0
    console.log(itemComparisonElementsItems)
    itemComparisonElementsItems.forEach((itemComparisonElement) => {
      if (itemComparisonElement.offsetHeight > comparisonMaxHeight) {
        comparisonMaxHeight = itemComparisonElement.clientHeight
      }
    })

    itemComparisonElementsItems.forEach((itemComparisonElement) => {
      itemComparisonElement.style.height = `${comparisonMaxHeight}px`
    })

    console.log("comparisonMaxHeight", comparisonMaxHeight)
  }
}, 5000)

setTimeout(() => {
  clearInterval(itemcComparisonInterval)
}, 10000)

const metricHeaderElements = document.getElementsByClassName(
  "outlook-item__metric-header"
)

const metricHeaderInterval = setInterval(() => {
  const metricHeaderElementsItems =
    Array.prototype.slice.call(metricHeaderElements)

  if (metricHeaderElements) {
    let metricHeaderMaxHeight = 0
    metricHeaderElementsItems.forEach((metricHeaderElement) => {
      if (metricHeaderElement.offsetHeight > metricHeaderMaxHeight) {
        metricHeaderMaxHeight = metricHeaderElement.clientHeight
      }
    })

    metricHeaderElementsItems.forEach((metricHeaderElement) => {
      metricHeaderElement.style.height = `${metricHeaderMaxHeight}px`
    })

    console.log("metricHeaderMaxHeight", metricHeaderMaxHeight)
  }
}, 5000)

setTimeout(() => {
  clearInterval(metricHeaderInterval)
}, 10000)

const subTextElements = document.getElementsByClassName("outlook-item__subtext")

const subTextInterval = setInterval(() => {
  const subTextElementsItems = Array.prototype.slice.call(subTextElements)

  if (subTextElements) {
    let subTextMaxHeight = 0
    subTextElementsItems.forEach((subTextElement) => {
      if (subTextElement.offsetHeight > subTextMaxHeight) {
        subTextMaxHeight = subTextElement.clientHeight
      }
    })

    subTextElementsItems.forEach((subTextElement) => {
      subTextElement.style.height = `${subTextMaxHeight}px`
    })

    console.log("subTextMaxHeight", subTextMaxHeight)
  }
})

setTimeout(() => {
  clearInterval(subTextInterval)
}, 10000)
